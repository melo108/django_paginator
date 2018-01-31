
class Mypaginator():
    '''
    id: 页码
    data:models数据
    perPageDateNum: 每页的数据量
    show_page_nums: 要展示的页码

    '''

    def __init__(self,data,id,perPageDateNum,show_page_nums):
        self.id=id
        self.data=data
        self.data_num=len(data)
        self.perPageDateNum=perPageDateNum
        self.show_page_nums=show_page_nums

    def get_page_range(self):
        page_num, mod = divmod(self.data_num, self.perPageDateNum)
        if mod:
            page_num += 1
        if self.id in range((self.show_page_nums + 1) // 2, page_num - (self.show_page_nums - 1) // 2 + 1):
            show_page_range = range(self.id - (self.show_page_nums - 1) // 2, self.id + (self.show_page_nums - 1) // 2 + 1)
        elif self.id < (self.show_page_nums + 1) // 2:
            show_page_range = range(1, self.show_page_nums + 1)
        else:
            show_page_range = range(page_num - self.show_page_nums + 1, page_num + 1)

        return show_page_range