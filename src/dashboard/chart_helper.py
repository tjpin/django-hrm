

def chart_helper(departments, gd, employees, gp):
    dps, genders, grades = {}, {}, {}

    for dp in departments:
        dps[dp.department] = 0
        if dp:
            for s in dp.staff_set.all():
                if s.department.department in dps.keys():
                    dps[s.department.department] += 1
        dps = {k: v for k,v in dps.items() if v != 0}

    for grade in gd:
        grades[grade.grade] = 0
        if grade:
            for g in grade.staff_set.all():
                if g.grade.grade in grades.keys():
                    grades[g.grade.grade] += 1
    grades = {k: v for k,v in grades.items() if v != 0}

    genders["Male"] = employees.filter(gender=gp.MALE).values_list().count()
    genders["Female"] = employees.filter(gender=gp.FEMALE).values_list().count()

    data = {
        "gender_labels": list(genders.keys()),
        "gender_data": list(genders.values()),
        "grades_labels": list(grades.keys()),
        "grades_data": list(grades.values()),
        "dept_labels": list(dps.keys()),
        "dept_data": list(dps.values()),
    }
    return data