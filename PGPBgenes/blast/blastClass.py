import subprocess
import os
from flask import current_app
from werkzeug.utils import secure_filename
import secrets
from multiprocessing import cpu_count


class Blast():
    def __init__(self, genome):
        self.threads = cpu_count()
        self.genome = genome
        self.temp_file_path = None

    def blast_search_file(self):
        blast_command = ['blastn', '-db', str(os.path.join(
            current_app.root_path, f"database/nucl/fasta_result")), '-query', self.temp_file_path, '-num_threads', str(self.threads), '-outfmt', '6']
                    
        p = subprocess.Popen(
            blast_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        return stdout, stderr

    def result_list_to_dict(self, result_list):
        """Given a blast result as a list of values, return a dictionary."""
        info_dict = {
            0: 'gene',
            1: 'subject_id',
            2: 'pct_identity',
            3: 'aln_length',
            4: "n_of_mismatches",
            5: "gap_openings",
            6: "q_start",
            7: "q_end",
            8: "s_start",
            9: "s_end",
            10: "e_value",
            11: "bit_score"
        }
        return {name: result_list[index] for index, name in info_dict.items()}

    def format_blast_output(self, raw_output):
        """Given raw blast output, convert to a list of lists, each sublist
        containing the output from one line."""
        output_lines = raw_output.split('\n')
        output_as_lists = [line.split() for line in output_lines if len(line)]
        return [self.result_list_to_dict(l) for l in output_as_lists]

    def save_temp_file(self, file):
        """Save file to temp folder"""
        filename = secure_filename(f'{secrets.token_hex(8)}_{file.filename}')
        tempfile_path = os.path.join(
            current_app.root_path, 'blast/temp', filename)
        file.save(tempfile_path)
        return tempfile_path

    def blast_search(self):
        """Perform a BLAST search for the given sequence. Format the result as JSON
        and return it."""
        tempfile_path = self.save_temp_file(self.genome)
        self.temp_file_path = tempfile_path
        stdout, stderr = self.blast_search_file()
        if stdout and stderr:
            json_output = self.format_blast_output(stdout.decode('utf-8'))
            os.remove(tempfile_path)
            return json_output, stderr.decode('utf-8')
        elif not stdout and not stderr:
            os.remove(tempfile_path)
            return None, {'stderr': 'No match found'}
        elif stdout and not stderr:
            json_output = self.format_blast_output(stdout.decode('utf-8'))
            os.remove(tempfile_path)
            return json_output, None
        else:
            os.remove(tempfile_path)
            return None, {'stderr': stderr.decode('utf-8')}
            
