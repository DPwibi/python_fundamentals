import ollama
def chat_with_deepseek(msg):
    """Function to chat with the DeepSeek model using Ollama."""
    res = ollama.chat(
        model="deepseek-r1:1.5b",
        messages=[
            {"role": "user", "content": msg}
        ]
    )
    return (res['message']['content'].replace('<think>', '').replace('</think>', '').strip())


def fahrenheit_2_celcius(f):
    c = (f - 32) * 5/9
    return c

def celcius_2_fahrenheit(c):
    f = (c*9/5) +32
    return f


def makesquare(tt,steps):
    tt.forward(steps)
    tt.left(90)
    tt.forward(steps)
    tt.left(90)
    tt.forward(steps)
    tt.left(90)
    tt.forward(steps)
    tt.left(90)




def move_up(local_turtle):
    local_turtle.setheading(90)


def move_left(TT):
    TT.setheading(180)

def move_down(TT):
    TT.setheading(270)

def move_right(TT):
    TT.setheading(0)







def rock_paper_scissors(computer, user):

    if computer == 'paper' and user == 'rock':
        print("computer won")
        return 'computer'

    if computer == 'paper' and user == 'paper':
        print("'Draw'")
        return 'Draw'

    if computer == 'rock' and user == 'rock':
        print("'Draw'")
        return 'Draw'

    if computer == 'scissors' and user == 'scissors':
        print("'Draw'")
        return 'Draw'

    if computer == 'rock' and user == 'scissors':
        print("computer won")
        return 'computer'

    if computer == 'scissors' and user == 'paper':
        print("computer won")
        return 'computer'

    if computer == 'paper' and user == 'scissors':
        print("user won")
        return 'user'

    if computer == 'scissors' and user == 'rock':
        print("user won")
        return 'user'

    if computer == 'rock' and user == 'paper':
        print("user won")
        return 'user'
    


def emoji_mood(word):
        moods = {
            "happy": "😊",
            "sad": "😢",
            "angry": "😠",
            "love": "❤️",
            "bored": "😐"
        }
        return moods.get(word.lower(), "🤔")
    

def reverse_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split())



def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True


