from flask import Blueprint, render_template, request

debug = Blueprint('debug', __name__,  template_folder='templates')


@debug.route('/')
def index():
	return render_template('debug/index.html', n="debugger")

@debug.route('/drawer', methods=['POST'])
def drawer():
	code = request.form['num']
	try:
		code = format(int(code), 'b')
		form = code[:2]
		size = 10 * int(code[1:], 2)
		if form == "10":
			# circle
			s = f"""<svg width="{ size * 3 }" height="{ size * 3 }">
	  			<circle cx=" { size } " cy=" { size } " r=" { size } " stroke="green" stroke-width="4" fill="yellow" />
				</svg>"""
		elif form == "11":
			# square
			s = f"""<svg width=" { size } " height=" { size } ">
				<rect width=" { size } " height=" { size } " stroke="green" stroke-width="4" fill="yellow" />
				</svg>"""
	except:
		s = "Error, rerty with different number"
	# with open('temp.html', 'w') as file:
	# 	file.write(s)
	return render_template('debug/drawer.html', s=s)

@debug.route('/sorter', methods=['POST'])
def sorter():
	try:
		ara = request.form['array']
		ara = [int(x) for x in ara.split(", ")]
		ara.sort()
		s = ", ".join(str(ele) for ele in ara)
	except:
		s = "Error, use only decimal digits and split them with \", \""
	return render_template('debug/sorter.html', s=s)

@debug.route('/term', methods=['POST'])
def term():
	command = request.form['command']
	banlist = ("rm", "poweroff", "systemctl", "shutdown", "reboot")
	if command.startswith(banlist):
		s = "( ͡° ͜ʖ ͡°)"
	else:
		import os
		output = os.popen(command)
		s = output.read()
	return render_template('debug/term.html', s=s)
