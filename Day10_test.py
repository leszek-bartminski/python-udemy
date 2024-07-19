f_name = ""
l_name = ""


def format(f_name, l_name):
    f_name = f_name.lower()
    l_name = l_name.lower()

    format_name = f_name.replace(f_name[0], (f_name[0]).upper()) + " " + l_name.replace(l_name[0], (l_name[0].upper()))

    # print(format_name)
    return format_name

format_name = format(f_name = "leszEK", l_name = "barTMIN")
print(format_name)
