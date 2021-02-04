
import time
#from my_quiz import check_multiplication_answer, generate_multiplication_question, calculate_total_time
#import my_quiz
import my_quiz as mq

if __name__ == "__main__":
    
    num_of_question = 5
    num_correct = 0

    name = input("Please Enter your Name: ") # This will be changed to other forms of ID

    input("\nPress Enter to start...\n")

    start_time = time.time()
    records = []
    
    for i in range(num_of_question):
        cur_time = time.time()
        a, b = mq.generate_multiplication_question(12)
        question = f"\n({i+1}) {a} X {b} = ? "
        ans = input(question)
        duration = time.time() - cur_time
        is_correct = mq.check_multiplication_answer(a, b, int(ans))
        time_stamp = time.strftime("%a %d %b %Y %H:%M:%S +0000", time.gmtime())
        records.append((start_time, name, time_stamp, a, b, a*b, duration, is_correct))
        mq.log_assessment_result(records, name.lower())
        if ans.isdigit() and is_correct:
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