import tkinter

class Main:
    def __init__(self) -> None:
        pass

    def main(self):
        global decimalField, binaryField
        tk = tkinter.Tk()
        tk.geometry("800x400")
        tk.title('Number system converter')
        binaryField = tkinter.Entry()
        binaryText = tkinter.Label(text='Binary')
        binaryText.pack(), binaryField.pack(pady=10)
        decimalField = tkinter.Entry()
        decimalText = tkinter.Label(text='Decimal system')
        decimalText.pack(), decimalField.pack(pady=10)
        convertButton = tkinter.Button(text='Convert binary to decimal', command=lambda: self.toDecimal(binaryField.get()))
        convertButton.pack(pady=10)
        convertdecButton = tkinter.Button(text='Convert decimal to binary', command=lambda: self.decimalToBinary(decimalField.get()))
        convertdecButton.pack(pady=10)
        clearButton = tkinter.Button(text='Clear all', command=self.clear)
        clearButton.pack()
        tk.mainloop()   

    def clear(self):
        decimalField.delete(0, tkinter.END)
        binaryField.delete(0, tkinter.END)

    def decimalToBinary(self, number):
        number = int(number)
        num = []
        res = ""
        while number >= 1:
            res=res+str(number%2)
            number //= 2
        num.append(res)
        num = self.listToString(num)
        num = num[::-1]
        binaryField.insert(0, str(num))

    def listToString(self, s): 
        temp = "" 
        
        for ele in s: 
            temp += str(ele)   
        return temp    

main = Main()
main.main()