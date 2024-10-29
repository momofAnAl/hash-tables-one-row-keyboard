def typing_time(layout, word):
    keyboards = {char:pos for pos, char in enumerate(layout)}
    
    
    location = 0
    total_time = 0
    for letter in word:
        next_location = keyboards[letter] 
        total_time += abs(next_location - location)
        location = next_location
        
    return total_time      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
    


