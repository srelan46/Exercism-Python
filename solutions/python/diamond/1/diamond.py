def rows(letter):
     if letter.upper()=='A':
         return ['A']
     num = ord(letter.upper())-ord('A')+1
     rows = num*2-1
     result = []
     for i in range(rows):
         if i==0:
             print("first")
             result.append(' '*(num-1)+'A'+' '*(num-1))
             print(result)
         elif i==rows-1:
             print("second")
             result.append(' '*(rows-num)+'A'+' '*(rows-num))
             print(result)
         else:
             if i<num:
                 print("3rd"+str(i))
                 current_letter = chr(ord('A') + i)

                 result.append(' ' * (num - i - 1) + current_letter + ' ' * (2 * i - 1) + current_letter+ ' ' * (num - i - 1))
                 print(result)
             else:
                 j = rows - 1 - i
                 print("4th"+str(i))
                 current_letter = chr(ord('A') + j)
                 result.append(' '*(num-j-1)+current_letter+' '*(2*j-1)+current_letter+' '*(num-j-1))
                 print(result)
     return result