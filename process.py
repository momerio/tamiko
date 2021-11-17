import sys
import time
import tamiko


def run():
    print()
    tamiko.start_process(process_name=sys._getframe().f_code.co_name)
    m = 20
    for i in range(1, m+1):
        sys.stdout.write("\033[2K\033[G["+"#"*i+" " *
                         (m-i)+"] {:0}".format(int(i/m*100))+"%")
        sys.stdout.flush()

        time.sleep(0.5)
    print()
    print()
    tamiko.end_process(process_name=sys._getframe().f_code.co_name)
