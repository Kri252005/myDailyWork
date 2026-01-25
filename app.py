from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Each task is now a dictionary to track 'task' text and 'status'
tasks = [] 

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_text = request.form.get('task')
    if task_text:
        tasks.append({'text': task_text, 'done': False}) # Track status
    return redirect('/')

@app.route('/edit/<int:index>', methods=['POST'])
def edit(index):
    new_text = request.form.get('new_text')
    if new_text:
        tasks[index]['text'] = new_text # Update logic
    return redirect('/')

@app.route('/done/<int:index>')
def done(index):
    tasks[index]['done'] = not tasks[index]['done'] # Track/Toggle status
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    tasks.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)