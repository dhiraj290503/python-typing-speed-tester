import time
import random


sentences = [
    "The quick brown fox jumps over the lazy dog.",     
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "I think, therefore I am."]

def typing_test():
    sentence = random.choice(sentences)
    print("Type the following sentence as fast as you can:")
    print(sentence)

    input("press enter when you are ready...")
    
    start_time = time.time()
    user_input = input("\nstart typing: \n")
    end_time = time.time()
    time_taken = end_time - start_time
    words_per_minute = len(user_input.split())

    print("results:")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Words typed: {words_per_minute}")   
    print(f"Typing speed: {words_per_minute / (time_taken / 60):.2f} words per minute")
    accuracy = sum(1 for a, b in zip(user_input, sentence) if a == b) / len(sentence) * 100
    print(f"Accuracy: {accuracy:.2f}%")

typing_test()