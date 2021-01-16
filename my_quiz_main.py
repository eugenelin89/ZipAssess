
import time
#from my_quiz import check_multiplication_answer, generate_multiplication_question, calculate_total_time
#import my_quiz
import my_quiz as mq

if __name__ == "__main__":
    
    num_of_question = 5
    num_correct = 0

    input("\nPress Enter to start...\n")

    start_time = time.time()
    
    for i in range(num_of_question):
        a, b = mq.generate_multiplication_question(12)
        question = f"\n({i+1}) {a} X {b} = ? "
        ans = input(question)

        if ans.isdigit() and mq.check_multiplication_answer(a, b, int(ans)):
            num_correct += 1
            print("Correct")
        else:
            print(f"Wrong... The answer is {a*b}.\n")
            print("\nG A M E   O V E R   ! ! !\n")
            break

    if num_correct == num_of_question:
        end_time = time.time()
        total_time = mq.calculate_total_time(start_time, end_time)

        print("\nFinished!\n")
        print(f"Time: {total_time} seconds")
        print(f"Score: {num_correct} out of {num_of_question}\n")