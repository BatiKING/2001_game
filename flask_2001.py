from flask import Flask
from flask import request
from Dice_simulator import dice_sim
import random

app = Flask(__name__)


@app.route("/2001", methods=['GET', 'POST'])
def game():
    p1_score = 0
    p2_score = 0
    # main game loop
    turn_count = 0
    modifier_text = ''
    if request.method == 'GET':
        return f"""
        <html>
            <body>
                <h1>Choose your dice and hit THROW to play</h1> <br>
                <form method="POST">
                    <input type="hidden" name="p1_score" value="{p1_score}">
                    <input type="hidden" name="p2_score" value="{p2_score}">
                    <input type="hidden" name="turn_count" value="{turn_count}">
                    <select name="die1">
                      <option value="D3">D3</option>
                      <option value="D4">D4</option>
                      <option value="D6">D6</option>
                      <option value="D8">D8</option>
                      <option value="D10">D10</option>
                      <option value="D12">D12</option>
                      <option value="D20">D20</option>
                      <option value="D100">D100</option>
                    </select>                        
                    <select name="die2">
                      <option value="D3">D3</option>
                      <option value="D4">D4</option>
                      <option value="D6">D6</option>
                      <option value="D8">D8</option>
                      <option value="D10">D10</option>
                      <option value="D12">D12</option>
                      <option value="D20">D20</option>
                      <option value="D100">D100</option>
                    </select>
                    <button type="submit">THROW</button>
                </form>
            </body>
        </html>
        """
    elif request.method == 'POST':
        p1_score = int(request.form['p1_score'])
        p2_score = int(request.form['p2_score'])



        p1_throw = 0
        p2_throw = 0
        p1_throw = dice_sim.throw_dice(request.form['die1'])
        p1_throw += dice_sim.throw_dice(request.form['die2'])
        turn_count = int(request.form['turn_count'])
        cpu_dice = cpu_dice_selection()
        p2_throw = dice_sim.throw_dice(cpu_dice[0])
        p2_throw += dice_sim.throw_dice(cpu_dice[1])
        p1_score += p1_throw
        p2_score += p2_throw

        if turn_count > 1:
            if p1_throw == 7:
                modifier_text += "<br> Your score is being divided by 7<br>"
                p1_score = p1_score // 7
            elif p1_throw == 11:
                modifier_text += "<br> Your score is being multiplied by 11<br>"
                p1_score = p1_score * 11

        if turn_count > 1:
            if p2_throw == 7:
                modifier_text += "<br> CPUs score is being divided by 7<br>"
                p2_score = p2_score // 7
            elif p2_throw == 11:
                modifier_text += "<br> CPUs score is being multiplied by 11<br>"
                p2_score = p2_score * 11

        turn_count += 1

        if p1_score > 2001:
            return f"<h1>You win! <br>Your score: {p1_score} <br> CPUs score: {p2_score} </h1>"
        if p2_score > 2001:
            return "<h1>CPU win!</h1> <br>Your score: {p1_score} <br> CPUs score: {p2_score} </h1>"

        return f"""
        <html>
            <body>
                <h1>Choose your dice and hit THROW to play</h1> <br>
                <h2> Your score: {p1_score}</h2> <br>
                <h2> CPUs score: {p2_score}</h2> <br>
                <br>
                <h2> This turn you've got {p1_throw}</h2> <br>
                <h2> This turn CPU's got {p2_throw}</h2> <br>
                {modifier_text}
                <h3> it's turn number {turn_count}</h3><br>
                
                <form method="POST">
                    <input type="hidden" name="p1_score" value="{p1_score}">
                    <input type="hidden" name="p2_score" value="{p2_score}">
                    <input type="hidden" name="turn_count" value="{turn_count}">
                    <select name="die1">
                      <option value="D3">D3</option>
                      <option value="D4">D4</option>
                      <option value="D6">D6</option>
                      <option value="D8">D8</option>
                      <option value="D10">D10</option>
                      <option value="D12">D12</option>
                      <option value="D20">D20</option>
                      <option value="D100">D100</option>
                    </select>                        
                    <select name="die2">
                      <option value="D3">D3</option>
                      <option value="D4">D4</option>
                      <option value="D6">D6</option>
                      <option value="D8">D8</option>
                      <option value="D10">D10</option>
                      <option value="D12">D12</option>
                      <option value="D20">D20</option>
                      <option value="D100">D100</option>
                    </select>
                    <button type="submit">THROW</button>
                </form>
            </body>
        </html>
        """


def cpu_dice_selection():
    available_dice = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    random.shuffle(available_dice)
    return available_dice[0], available_dice[1]


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
