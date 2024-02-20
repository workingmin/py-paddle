from paddlenlp import Taskflow

if __name__ == '__main__':
    summarizer = Taskflow("text_summarization")
    summarizer('2022年，中国房地产进入转型阵痛期，传统“高杠杆、快周转”的模式难以为继，万科甚至直接喊话，中国房地产进入“黑铁时代”')
