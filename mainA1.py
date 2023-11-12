from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
#A1G
@app.route('/a1g')
def a1g_description():
    description = "Beispiel A1G"
    return description

#A1F
@app.route('/immutable-values', methods=['GET'])
def immutable_values():
    explanation = (
        "test"
    )
    return {'explanation': explanation}

#A1E
# Objektorientierte Lösung
class ProblemSolverOO:
    def __init__(self, problem):
        self.problem = problem

    def solve(self):
        # Hier wird das Problem objektorientiert gelöst
        return f"Objektorientierte Lösung: {self.problem}"

# Prozedurale Lösung
def solve_problem_procedural(problem):
    # Hier wird das Problem prozedural gelöst
    return f"Prozedurale Lösung: {problem}"

# Funktionale Lösung
def solve_problem_functional(problem):
    # Hier wird das Problem funktional gelöst
    return f"Funktionale Lösung: {problem}"

@app.route('/solve_oo')
def solve_oo():
    problem_solver = ProblemSolverOO("OO-Problem")
    return problem_solver.solve()


@app.route('/solve_procedural')
def solve_procedural():
    problem = "Prozedurales Problem"
    return solve_problem_procedural(problem)


@app.route('/solve_functional')
def solve_functional():
    problem = "Funktionales Problem"
    return solve_problem_functional(problem)

#B1G



if __name__ == '__main__':
    app.run(debug=True)