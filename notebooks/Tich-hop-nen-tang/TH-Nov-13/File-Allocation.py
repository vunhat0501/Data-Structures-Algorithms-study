import random

class FileManager:
    def __init__(self):
        self.free_blocks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.files = {} 

    def allocate_linked(self, filename, n_blocks):
        if len(self.free_blocks) < n_blocks:
            print(f"Loi: Khong du block trong de tao file '{filename}'.")
            return

        chosen_blocks = random.sample(self.free_blocks, n_blocks)
        for b in chosen_blocks:
            self.free_blocks.remove(b)
        
        self.files[filename] = {
            "type": "Linked",
            "data": chosen_blocks
        }
        print(f" Da tao file '{filename}' (Linked): {chosen_blocks}")

    def allocate_indexed(self, filename, n_blocks):
        # Cần n block dữ liệu + 1 block làm index
        if len(self.free_blocks) < n_blocks + 1:
            print(f" Loi: Khong du block trong de tao file '{filename}'.")
            return

        chosen = random.sample(self.free_blocks, n_blocks + 1)
        index_block = chosen[0]
        data_blocks = chosen[1:]

        for b in chosen:
            self.free_blocks.remove(b)

        self.files[filename] = {
            "type": "Indexed",
            "index_block": index_block,
            "data_blocks": data_blocks
        }
        print(f" Da tao file '{filename}' (Indexed). Index Block: {index_block} -> Data: {data_blocks}")

    def read_file(self, filename):
        if filename not in self.files:
            print(f" File '{filename}' không ton tai.")
            return
        
        f_info = self.files[filename]
        print(f" Doc file '{filename}':")
        if f_info["type"] == "Linked":
            chain = " -> ".join(map(str, f_info["data"]))
            print(f"   Start -> {chain} -> End")
        else:
            print(f"   Index Block [{f_info['index_block']}] tro toi: {f_info['data_blocks']}")

    def delete_file(self, filename):
        if filename not in self.files:
            print(f"File '{filename}' khong ton tai.")
            return

        f_info = self.files[filename]
        returned_blocks = []
        
        if f_info["type"] == "Linked":
            returned_blocks = f_info["data"]
        else:
            returned_blocks = [f_info["index_block"]] + f_info["data_blocks"]

        self.free_blocks.extend(returned_blocks)
        self.free_blocks.sort() 
        del self.files[filename]
        
        print(f" Da xoa file '{filename}'. Free blocks hien tai: {self.free_blocks}")

if __name__ == "__main__":
    print("\n FILE ALLOCATION")
    fm = FileManager()
    print(f"Free blocks ban dau: {fm.free_blocks}")

    fm.allocate_linked("File_A", 3)
    fm.read_file("File_A")
    
    fm.allocate_indexed("File_B", 2) 
    fm.read_file("File_B")

    fm.delete_file("File_A")
    
    fm.allocate_linked("File_C", 4)
    fm.read_file("File_C")