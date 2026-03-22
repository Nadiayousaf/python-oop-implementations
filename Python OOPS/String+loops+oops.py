# Task 1:
def length_checker():
    username=input("Enter username:")
    if len(username)>=5:
        print("invalid username")
length_checker()

# Task 2:
def email_domain_extractor():
    gmail=input("Enter gmail:")
    domain=gmail.split("@")[-1]
    print(domain)
email_domain_extractor()

#Task 3:
def count_letter():
    letter=input("Enter the letter: ")
    upper=0
    lower=0
    for char in letter:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1
    print("Upper_case:",upper)
    print("Lowwer_case:",lower)
count_letter()


#Task 4:
def text_analyzer():
    text=input("Enter the text :")
    words=text.split()
    count=0
    for word in words:   
       count+=1
    print("Total Words",count,end="")
text_analyzer()



#tASK 5




def chat_message_analyzer():
    text=input("Enter the text: ")
    def count_words(text):
        words=text.split()
        count=0
        for word in words:
            count+=1
        print("Total_Words: ", count) 
        
    def total_char(text):
        count=0
        for char in text:
            if char !=" ":   
             count+=1
        print("Total char: ",count)
        
    def count_vowels(text):
        vowels="aeiou"
        count=0
        for char in text:
            if char in vowels:
                count+=1
        print("Vowels:",count)
        
    def count_digits(text):
        count=0
        for char in text:
            if char.isdigit():
                count+=1
        print("Total Digits:",count)
        
    def longest_word(text):
        words=text.split()
        longest=""
        for word in words:
            if len(word)>len(longest):
                longest=word
        print("Longest Word: ",longest)
    longest_word(text)
    count_digits(text)
    count_vowels(text)
    total_char(text)
    count_words(text)
chat_message_analyzer()
        
        
        
# task 6:

def chat_message_analyzer():
    text=input("Enter the text:")
    words=text.split()
    longest_word = max(words, key=len) if words else ""
    total_words=len(words)
    
    vowels_count=0
    digits_count=0
    chars_count=0
    
    for char in text:
        if char!="":
            chars_count+=1
        if char.lower() in "aeiou":
            vowels_count+=1
        if char.isdigit():
            digits_count+=1
            
            
    print("Total Words:", total_words)
    print("Total Characters (no spaces):", chars_count)
    print("Vowels:", vowels_count)
    print("Digits:", digits_count)
    print("Longest Word:", longest_word)
    
chat_message_analyzer()

            
# tASK 7: with classes and objects :
 

class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def word_count(self):
        return len(self.text.split())

    def longest_word(self):
        words = self.text.split()
        return max(words, key=len) if words else ""

    def char_count(self):
        return sum(1 for char in self.text if char != " ")

    def vowel_count(self):
        return sum(1 for char in self.text.lower() if char in "aeiou")

    def digit_count(self):
        return sum(1 for char in self.text if char.isdigit())

    def analyze(self):
        print("Total Words:", self.word_count())
        print("Total Characters (no spaces):", self.char_count())
        print("Vowels:", self.vowel_count())
        print("Digits:", self.digit_count())
        print("Longest Word:", self.longest_word())


"""   # Usage
text_input = input("Enter the text: ")
analyzer = TextAnalyzer(text_input)
analyzer.analyze()

Exactly — in both cases you input text once and get all results. The **difference is not about input**, it’s about **structure, reusability, and scalability**:

* **Nested functions:** everything exists only when that function runs; you can’t reuse its logic elsewhere or easily create multiple analyzers.
* **Class:** the text is stored in the object, and all methods can access it anytime; you can create **many objects** for different texts and reuse the methods independently.

✅ So input looks the same, but **class makes the code reusable, organized, and extendable** for bigger projects.    """


        
        