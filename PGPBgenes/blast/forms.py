from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.simple import FileField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import ValidationError


def FileSizeLimit(max_size_in_mb):
    max_bytes = max_size_in_mb * 1024 * 1024

    def _file_length_check(form, field):
        if len(field.data.read()) > max_bytes:
            raise ValidationError(f"File size must be less than {max_size_in_mb}MB")

    return _file_length_check

class BlastForm(FlaskForm):
    genome = FileField('Upload fasta file', validators=[FileRequired(), FileAllowed(['fasta'])])
    
    submit = SubmitField('BLAST')
