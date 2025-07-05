def createLessonPlan(course, para, content, data, callWord):
    """
    course:课程名，string
    para:章节名，string
    content:目录，一个string数组
    data:大纲内容，string
    callWord:用户输入的提示词，string

    返回一个string，代表教案的数据，为html格式（告诉ai，他知道什么意思）
    """
    print(course, para, content, data, callWord)
    return "这是生成的教案"


if __name__ == "__main__":
    createLessonPlan(
        "软件工程",
        "软件生命周期与过程模型",
        ["课程目的", "课程内容", "课程总结"],
        "介绍软件生命周期的不同阶段（需求分析、设计、编码、测试、维护等），探讨瀑布模型、迭代模型、敏捷开发等多种过程模型及其适用场景。",
        "帮我生成一份教案，其中重点介绍敏捷开发",
    )
