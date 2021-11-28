from tkinter import *
from tkinter import ttk

class Output:
    def __init__ (self, result_arr, method_name, execution_time):
        self.result_arr = result_arr
        self.method_name = method_name
        self.execution_time = execution_time
    
    def showOutput(self):
        root = Tk()
        root.title("Output of " + self.method_name)
        root.geometry("900x500")

        number_of_iterations = len(self.result_arr)
        Label(root, text="Number of Iterations: {}".format(number_of_iterations)).pack()
        Label(root, text="Execution Time: {}".format(self.execution_time)).pack()
        result_frame = Frame(root)
        result_frame.pack()
        result = ttk.Treeview(result_frame)

        result["columns"] = ("iteration", "x_prev", "x", "f(x)", "error")

        result.column("#0", width=0, stretch=NO)
        result.column("iteration", anchor=CENTER, width=80)
        result.column("x_prev", anchor=CENTER, width=200)
        result.column("x", anchor=CENTER, width=200)
        result.column("f(x)", anchor=CENTER, width=200)
        result.column("error", anchor=CENTER, width=200)

        result.heading("#0", text="", anchor=CENTER)
        result.heading("iteration", text="Iteration", anchor=CENTER)
        result.heading("x_prev", text="Prev. X", anchor=CENTER)
        result.heading("x", text="X", anchor=CENTER)
        result.heading("f(x)", text="F(X)", anchor=CENTER)
        result.heading("error", text="Error", anchor=CENTER)


        for i in range(len(self.result_arr)):
            result.insert(parent='', index='end', iid=i, values=self.result_arr[i])
        result.pack()
        root.mainloop()

        