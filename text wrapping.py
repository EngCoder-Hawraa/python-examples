import textwrap

value = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the """
wrapper = textwrap.TextWrapper(width=60)
word_list = wrapper.wrap(text=value)

for element in word_list:
    print(element)