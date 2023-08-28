import random

def generate_mistake(word):
    if len(word) <= 1:
        return word
    
    idx = random.randint(0, len(word) - 1)
    new_word = word[:idx] + random.choice('abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç') + word[idx+1:]
    return new_word

def generate_mistakes(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            word = line.strip()
            mistake = generate_mistake(word)
            f_out.write(f"{word} {mistake}\n")

# Chamada da função
input_file = 'Base/words-utf-8.txt'  # Substitua pelo nome do arquivo de entrada
output_file = 'Base/output-utf-8.txt'      # Substitua pelo nome do arquivo de saída
generate_mistakes(input_file, output_file)