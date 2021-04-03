from matplotlib import pyplot as plt
import pandas as pd

class VariantTable:
    def __init__(self, mutation_list_path, mutation_list_type, mutation_head, output_path, output_type):
        self.mutation_file = pd.read_table(mutation_list_path, mutation_list_type)
        self.output = pd.read_table(output_path, output_type)
        self.mutations = self.mutation_file[mutation_head]
        self.table = pd.concat([self.mutations, self.output])
    def return_cols(self, cols):
        columns = self.table[cols]
        return columns


class PlotVariants:
    def __init__(self, x, y, x_lab, y_lab, plt_type, title):
        self.x = x
        self.y = y
        self.x_lab = x_lab
        self.y_lab = y_lab
        self.plt_type = plt_type
        self.title = title
    def make_plot(self):
        plt.plot(self.x,self.y)
        plt.title(self.title)
        plt.xlabel(self.x_lab)
        plt.ylabel(self.y_lab)
        plt.show()

def main():
    pass

if __name__ == "__main__":
    main()
