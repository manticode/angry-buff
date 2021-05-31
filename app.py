import os
from copy import copy
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators

""" Small app to take list of player names and allocate group assignments according to raid size. """

__author__ = 'Leondréa-Mirage Raceway'
__version__ = '0.1'

app = Flask(__name__)
app.secret_key = os.urandom(31)


class InputPriestForm(FlaskForm):
    priests_list = TextAreaField('List of Priests')
    raid_group_qty = StringField('Group quantity')
    submit_btn = SubmitField('GO!')


def create_groups(group_qty):
    """ Create list of groups. Sanitise anything silly (WoW groups are 1-8). """
    if group_qty > 8 or not group_qty or group_qty == 0:
        raise Exception('Group quantity must be between 1 and 8.')
    group_list = []
    for x in range(0, group_qty):
        group_list.append(x+1)
    return group_list


def cleanse_priest_list(priests_list):
    """ Take WTForms list and cleanse it for processing. """


def construct_assignments(priest_list, group_list):
    """ Map priests to a group and return dict for outputting. """
    priest_list = copy(priest_list)
    group_list = copy(group_list)
    buff_assignments = []
    if len(priest_list) == len(group_list):
        """ 1 priest per group """
        priest_group = zip(priest_list, group_list)
        for priest_assign in priest_group:
            priest, group = priest_assign
            buff_assignments.append({"priest": priest, "groups_assigned": [group]})
    elif len(priest_list) < len(group_list):
        """ Fewer priests than groups, some will have more than 1 group assigned. 
            Function will attempt to give consecutive group assignments in these cases. """
        priest_parties_each, priest_additionals = divmod(len(group_list), len(priest_list))
        for priest in priest_list:
            buff_allocation = {"priest": priest, "groups_assigned": []}
            if priest_additionals > 0:
                for x in range(priest_parties_each+1):
                    group_pop = group_list.pop(0)
                    buff_allocation["groups_assigned"].append(group_pop)
                priest_additionals -= 1
            else:
                for x in range(priest_parties_each):
                    group_pop = group_list.pop(0)
                    buff_allocation["groups_assigned"].append(group_pop)
            buff_assignments.append(buff_allocation)
        print("Outcome: ", buff_assignments)
    return buff_assignments


@app.route('/', methods=['GET', 'POST'])
def main_page():
    form = InputPriestForm()
    if request.method == 'GET':
        return render_template('index.html', form=form)
    elif request.method == 'POST':
        priest_list = form.priests_list.data
        raid_size = form.raid_group_qty.data
        print(priest_list, raid_size)
        return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
