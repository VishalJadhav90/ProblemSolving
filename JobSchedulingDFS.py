def __find_dependencies(project, dependencies):
    dep_list = []
    for non_dep, dep in dependencies:
        if dep == project:
            dep_list.append(non_dep)
    return dep_list


def generate_schedule(job, dep_dict, sch, local_sch, local_job):
    if job == local_job and local_job in local_sch:
        return "ERROR"
    local_sch.append(job)
    if dep_dict[job] and job not in sch:
        for dep_proj in dep_dict[job]:
            result = generate_schedule(dep_proj, dep_dict, sch, local_sch, local_job)
            if result:
                return result
        if job not in sch:
            sch.append(job)
    elif job not in sch:
        sch.append(job)

def print_build_order(projects, dependencies, dep_dict):
    for project in projects:
        dep_dict[project] = []
        for dep in __find_dependencies(project, dependencies):
            dep_dict[project].append(dep)
    sch = []
    for job in dep_dict:
        local_sch = []
        result = generate_schedule(job, dep_dict, sch, local_sch, job)
        if result:
            print(result)
            return
    print(sch)

projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c'), ('c', 'd')]
dep_dict = {}
print_build_order(projects, dependencies, dep_dict)
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
dep_dict = {}
print_build_order(projects, dependencies, dep_dict)
