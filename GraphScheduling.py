def __find_dependencies(project, dependencies):
    dep_list = []
    for non_dep, dep in dependencies:
        if dep == project:
            dep_list.append(non_dep)
    return dep_list

def __non_dependent_project(dep_dict):
    non_dependent_proj_list = []
    for proj, dependencies in dep_dict.items():
        if not dependencies:
            non_dependent_proj_list.append(proj)
    return non_dependent_proj_list

def generate_build_order(dep_dict):
    scheduled_proj_list = []
    while dep_dict:
        non_dep_proj = __non_dependent_project(dep_dict)
        if not non_dep_proj and dep_dict:
            return []
        scheduled_proj_list.extend(non_dep_proj)
        for proj in non_dep_proj:
            dep_dict.pop(proj)
            for proj in dep_dict:
                deps = dep_dict[proj]
                for dep in deps:
                    if dep in non_dep_proj:
                        deps.remove(dep)
    return scheduled_proj_list

def print_build_order(projects, dependencies, dep_dict):
    for project in projects:
        dep_dict[project] = []
        for dep in __find_dependencies(project, dependencies):
            dep_dict[project].append(dep)
    print(generate_build_order(dep_dict))

projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
dep_dict = {}
print_build_order(projects, dependencies, dep_dict)