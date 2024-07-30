import sys
sys.path.append('/Users/mmehra/gitrepos/UserAssignment')

from flask import Flask, render_template, redirect, url_for, flash
from forms import AdminForm, ParticipantForm
from models import user_manager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = AdminForm()
    if form.validate_on_submit():
        prefix = form.prefix.data
        start = form.start.data
        end = form.end.data
        user_manager.generate_usernames(prefix, start, end)
        flash('Usernames generated successfully', 'success')
        return redirect(url_for('admin'))
    return render_template('admin.html', form=form, available_usernames=user_manager.available_usernames, assigned_usernames=user_manager.assigned_usernames)

@app.route('/participant', methods=['GET', 'POST'])
def participant():
    form = ParticipantForm()
    if form.validate_on_submit():
        workshop_username = form.workshop_username.data
        assigned_username = user_manager.assign_username(workshop_username)
        if assigned_username:
            flash(f'Your assigned username is {assigned_username}', 'success')
        else:
            flash('No available usernames', 'danger')
        return redirect(url_for('participant'))
    return render_template('participant.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

