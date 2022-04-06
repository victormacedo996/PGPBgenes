from datetime import datetime
from flask import flash, redirect, render_template, Blueprint, url_for, redirect
from PGPBgenes.blast.forms import BlastForm #, CreateDBForm
from PGPBgenes.blast.blastClass import Blast #, CreateDB

blast = Blueprint('blast', __name__)


@blast.route("/en/blast", methods=['GET', 'POST'])
def home_en():
    date = datetime.now()
    blast_form = BlastForm()
    # database_form = CreateDBForm()
    if blast_form.validate_on_submit():
        # db = { key: value for key, value in blast_form.data.items() if 'prot_databases' or 'nucl_databases' in key }
        blast = Blast(genome=blast_form.data['genome'])
        blast, error = blast.blast_search()
        return render_template('en/blast_result_en.html', title='Blast result', blast_form=blast_form, blast=blast, error=error, blast_result=True, date=date.year)
    
    # if database_form.validate_on_submit():
    #     db = CreateDB(database=database_form.data['database'], db_type=database_form.data['database_type'])
    #     stdout, stderr = db.create_db()
    #     if stdout and not stderr:
    #         flash(stdout, 'success')
    #     elif stdout and stderr:
    #         flash(stdout, 'success')
    #         flash(stderr, 'danger')
    #     elif not stdout and stderr:
    #         flash(stderr, 'danger')
    #     elif not stdout and not stderr:
    #         flash('Some unespected error occured', 'warning')
    #     return redirect(url_for('main.home_en'))

    return render_template('en/blast_en.html', title='Blast', blast_form=blast_form, date=date.year) #, database_form=database_form)


@blast.route("/pt_br/blast", methods=['GET', 'POST'])
def home_pt_br():
    date = datetime.now()
    blast_form = BlastForm()
    # database_form = CreateDBForm()
    if blast_form.validate_on_submit():
        db = { key: value for key, value in blast_form.data.items() if 'prot_databases' or 'nucl_databases' in key }
        blast = Blast(genome=blast_form.data['genome'], db=db)
        blast, error = blast.blast_search()
        if error:
            if error['stderr'] == 'No match found':
                error['stderr'] = 'Nenhuma correspondencia encontrada'
        return render_template('pt_br/blast_result_pt_br.html', title='Resultados do Blast', blast_form=blast_form, blast=blast, error=error, blast_result=True, date=date.year)
    
    # if database_form.validate_on_submit():
    #     db = CreateDB(database=database_form.data['database'], db_type=database_form.data['database_type'])
    #     stdout, stderr = db.create_db()
    #     if stdout and not stderr:
    #         flash(stdout, 'success')
    #     elif stdout and stderr:
    #         flash(stdout, 'success')
    #         flash(stderr, 'danger')
    #     elif not stdout and stderr:
    #         flash(stderr, 'danger')
    #     elif not stdout and not stderr:
    #         flash('Um erro inesperado ocorreu', 'warning')
    #     return redirect(url_for('main.home_pt_br'))

    return render_template('pt_br/blast_pt_br.html', title='Blast', blast_form=blast_form, date=date.year) #,  database_form=database_form )

