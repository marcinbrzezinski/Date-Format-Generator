# Date-Format-Generator

## Info

This simple script generates a list of dates in different formats. You can specify a list of dates and generate combinations of them.

## Example

 I defined a list with two dates: **24/09/2017** and **01/09/2017**
    
    dates = [(2017, 9, 24), (2017, 10, 1)]

and separators:

    sep = ["/", "-", ".", " ", "\\"]

The output is stored in *Dates_list.txt* file. You can set how dates are separated. I set the default ' ', but if you need, just change space character in function *write_to_file*
    
    def write_to_file(dl):
      file = open('Dates_list.txt', 'w')

      try:
          file.write(' '.join(dl))
        
      finally:
          file.close()

**For every date in new line:**
     
     file.write('\n'.join(dl))

**For dates separated by '&&':**
      
     file.write(' && '.join(dl))
    
As you can see, you can specify exactly what you need.

## Output file

Date in new line:
 
    17/Sep/24
    17-Sep-24
    17.Sep.24
    17 Sep 24
    17\Sep\24
    24/Sep/17
    24-Sep-17
    24.Sep.17
    24 Sep 17
    24\Sep\17
    Sep/24/17
    Sep-24-17
    Sep.24.17
    Sep 24 17
    Sep\24\17
    17/September/24
    17-September-24
    17.September.24
    17 September 24
    17\September\24
    24/September/17
    24-September-17
    24.September.17
    24 September 17
    24\September\17
    September/24/17
    September-24-17
    September.24.17
    September 24 17
    September\24\17
    17/09/24
    17-09-24
    17.09.24
    17 09 24
    17\09\24
    24/09/17
    24-09-17
    24.09.17
    24 09 17
    24\09\17
    09/24/17
    09-24-17
    09.24.17
    09 24 17
    09\24\17
    2017/Sep/24
    2017-Sep-24
    2017.Sep.24
    2017 Sep 24
    2017\Sep\24
    24/Sep/2017
    24-Sep-2017
    24.Sep.2017
    24 Sep 2017
    24\Sep\2017
    Sep/24/2017
    Sep-24-2017
    Sep.24.2017
    Sep 24 2017
    Sep\24\2017
    2017/September/24
    2017-September-24
    2017.September.24
    2017 September 24
    2017\September\24
    24/September/2017
    24-September-2017
    24.September.2017
    24 September 2017
    24\September\2017
    September/24/2017
    September-24-2017
    September.24.2017
    September 24 2017
    September\24\2017
    2017/09/24
    2017-09-24
    2017.09.24
    2017 09 24
    2017\09\24
    24/09/2017
    24-09-2017
    24.09.2017
    24 09 2017
    24\09\2017
    09/24/2017
    09-24-2017
    09.24.2017
    09 24 2017
    09\24\2017
    17/Oct/01
    17-Oct-01
    17.Oct.01
    17 Oct 01
    17\Oct\01
    01/Oct/17
    01-Oct-17
    01.Oct.17
    01 Oct 17
    01\Oct\17
    Oct/01/17
    Oct-01-17
    Oct.01.17
    Oct 01 17
    Oct\01\17
    17/October/01
    17-October-01
    17.October.01
    17 October 01
    17\October\01
    01/October/17
    01-October-17
    01.October.17
    01 October 17
    01\October\17
    October/01/17
    October-01-17
    October.01.17
    October 01 17
    October\01\17
    17/10/01
    17-10-01
    17.10.01
    17 10 01
    17\10\01
    01/10/17
    01-10-17
    01.10.17
    01 10 17
    01\10\17
    10/01/17
    10-01-17
    10.01.17
    10 01 17
    10\01\17
    2017/Oct/01
    2017-Oct-01
    2017.Oct.01
    2017 Oct 01
    2017\Oct\01
    01/Oct/2017
    01-Oct-2017
    01.Oct.2017
    01 Oct 2017
    01\Oct\2017
    Oct/01/2017
    Oct-01-2017
    Oct.01.2017
    Oct 01 2017
    Oct\01\2017
    2017/October/01
    2017-October-01
    2017.October.01
    2017 October 01
    2017\October\01
    01/October/2017
    01-October-2017
    01.October.2017
    01 October 2017
    01\October\2017
    October/01/2017
    October-01-2017
    October.01.2017
    October 01 2017
    October\01\2017
    2017/10/01
    2017-10-01
    2017.10.01
    2017 10 01
    2017\10\01
    01/10/2017
    01-10-2017
    01.10.2017
    01 10 2017
    01\10\2017
    10/01/2017
    10-01-2017
    10.01.2017
    10 01 2017
    10\01\2017

    
