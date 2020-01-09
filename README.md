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
