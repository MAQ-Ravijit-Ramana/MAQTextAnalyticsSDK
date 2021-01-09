class BatchSetup():
    """
    Logic for mapping list to expected input json
    :param list data: User text corpus
    """
    def __init__(self,data):
        if(isinstance(data,list)):
            self.data = data
        else:
            raise TypeError
    
    def makeBody(self):
        """
        makeBody
        :return: dict of user corpus
        """
        dataList = []
        dataInput = dict()
        for idx,data in enumerate(self.data):
            dataDict = dict()
            dataDict['id'] = str(idx)
            dataDict['text'] = str(data)
            dataList.append(dataDict)
        dataInput['data'] = dataList
        return dataInput