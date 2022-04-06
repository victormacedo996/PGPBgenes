from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.simple import FileField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import ValidationError
# from wtforms import RadioField
# from wtforms.validators import InputRequired
# from flask import current_app
# import os


# create form to submit gene sequence to BLAST model

def FileSizeLimit(max_size_in_mb):
    max_bytes = max_size_in_mb * 1024 * 1024

    def _file_length_check(form, field):
        if len(field.data.read()) > max_bytes:
            raise ValidationError(f"File size must be less than {max_size_in_mb}MB")

    return _file_length_check

# def db_names():
#     file_path = os.path.abspath(os.path.dirname(__file__))
#     nucl_db_path = f'{file_path}/../database/nucl'
#     prot_db_path = f'{file_path}/../database/prot'
#     nucl_dbs = [nucl_db for nucl_db in os.listdir(nucl_db_path) if nucl_db.endswith('.nhr')]
#     prot_dbs = [prot_db for prot_db in os.listdir(prot_db_path) if prot_db.endswith('.phr')]
#     return prot_dbs, nucl_dbs

class BlastForm(FlaskForm):
    # gene_sequence = StringField('Gene sequence', validators=[DataRequired()])
    genome = FileField('Upload fasta file', validators=[FileRequired(), FileAllowed(['fasta'])])
    # prot_db_names, nucl_db_names = db_names()
    # if nucl_db_names:
    #     nucl_databases = RadioField('Nucleotides databases', choices=[(db_name.replace('.nhr', ''), db_name.replace('.nhr', '')) for db_name in nucl_db_names])
    # if prot_db_names:        
    #     prot_databases = RadioField('Protein databases', choices=[(db_name.replace('.phr', ''), db_name.replace('.phr', '')) for db_name in prot_db_names])
    
    submit = SubmitField('BLAST')

# class CreateDBForm(FlaskForm):
#     database = FileField('Upload fasta file', validators=[FileRequired(), FileAllowed(['fasta'])])
#     database_type = RadioField('Database type', choices=[('nucleotide','nucleotide'),('protein','protein')], validators=[InputRequired()])
#     submit = SubmitField('create db')