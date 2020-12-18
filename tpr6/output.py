from task1 import reflexivity, antireflexivity, symmetry, connectivity, antisymmetry, transitivity, asymmetry, \
    quasi_equivalence, indifference, alpha_level, association, intersection, complement, composition, strict


def print_task1(r, s):
    rs_association = association(r, s)
    rs_intersection = intersection(r, s)
    r_complement = complement(r)
    s_complement = complement(s)
    rs_composition = composition(r, s)
    r_alpha_level_05 = alpha_level(r, 0.5)
    r_alpha_level_09 = alpha_level(r, 0.9)
    r_strict = strict(r)
    for i in range(len(r_strict)):
        for j in range(len(r_strict)):
            r_strict[i][j] = round(r_strict[i][j])
    r_indifference = indifference(r)
    r_quasi_equivalence = quasi_equivalence(r)
    print()
    print("Об'єднання R1 та R2:\n")
    for i in rs_association:
        for j in i:
            print(j, end=' ')
        print()
    print()
    print("Перетин R1 та R2:\n")
    for i in rs_intersection:
        for j in i:
            print(j, end=' ')
        print()
    print()
    print("Доповнення R1:\n")
    for i in r_complement:
        for j in i:
            print(j, end=' ')
        print()
    print()
    print("Доповнення R2:\n")
    for i in s_complement:
        for j in i:
            print(j, end=' ')
        print()
    print()
    print("Композиція R1 та R2:\n")
    for i in rs_composition:
        for j in i:
            print(j, end=' ')
        print()
    print()
    print("Альфа-рівень 0.5 відношення R1:\n")
    for i in r_alpha_level_05:
        for j in i:
            print(j, end=' ')
        print()
    print()
    print("Альфа-рівень 0.9 відношення R1:\n")
    for i in r_alpha_level_09:
        for j in i:
            print(j, end=' ')
        print()
    print()
    print("Відношення строгої переваги для R1:\n")
    for i in r_strict:
        for j in i:
            print(j, end=' ')
        print()
    print()
    print("Відношення байдужості для R1:\n")
    for i in r_indifference:
        for j in i:
            print(j, end=' ')
        print()
    print()
    print("Відношення квазіеквівалентності для R1:\n")
    for i in r_quasi_equivalence:
        for j in i:
            print(j, end=' ')
        print()


def print_properties(r1, r2):
    r1_strong_ref, r1_slight_ref = reflexivity(r1)
    r2_strong_ref, r2_slight_ref = reflexivity(r2)
    r1_strong_antiref, r1_slight_antiref = antireflexivity(r1)
    r2_strong_antiref, r2_slight_antiref = antireflexivity(r2)
    r1_sym = symmetry(r1)
    r2_sym = symmetry(r2)
    r1_antisym = antisymmetry(r1)
    r2_antisym = antisymmetry(r2)
    r1_asym = asymmetry(r1)
    r2_asym = asymmetry(r2)
    r1_strong_con, r1_slight_con = connectivity(r1)
    r2_strong_con, r2_slight_con = connectivity(r2)
    r1_trans = transitivity(r1)
    r2_trans = transitivity(r2)
    print()
    print("Рефлексивність:")
    print()
    print("R1:")
    if r1_strong_ref:
        print("Властивість сильної рефлексивності присутня")
    elif r1_slight_ref:
        print("Властивість слабкої рефлексивності відсутня")
    else:
        print("Властивість рефлексивності відсутня")
    print("R2:")
    if r2_strong_ref:
        print("Властивість сильної рефлексивності присутня")
    elif r2_slight_ref:
        print("Властивість слабкої рефлексивності присутня")
    else:
        print("Властивість рефлексивності відсутня")
    print()
    print("Антирефлексивність:")
    print()
    print("R1:")
    if r1_strong_antiref:
        print("Властивість сильної антирефлексивності присутня")
    elif r1_slight_antiref:
        print("Властивість слабкої антирефлексивності присутня")
    else:
        print("Властивість антирефлексивності відсутня")
    print("R2:")
    if r2_strong_antiref:
        print("Властивість сильної антирефлексивності присутня")
    elif r2_slight_antiref:
        print("Властивість слабкої антирефлексивності присутня")
    else:
        print("Властивість антирефлексивності відсутня")
    print()
    print("Симетричність:")
    print()
    print("R1:")
    if r1_sym:
        print("Властивість сильної симетричності присутня")
    else:
        print("Властивість симетричності відсутня")
    print("R2:")
    if r2_sym:
        print("Властивість сильної симетричності присутня")
    else:
        print("Властивість симетричності відсутня")
    print()
    print("Антисиметричність:")
    print()
    print("R1:")
    if r1_antisym:
        print("Властивість сильної антисиметричності присутня")
    else:
        print("Властивість антисиметричності відсутня")
    print("R2:")
    if r2_antisym:
        print("Властивість сильної антисиметричності присутня")
    else:
        print("Властивість сильної антисиметричності відсутня")
    print()
    print("Асиметричність:")
    print()
    print("R1:")
    if r1_asym:
        print("Властивість сильної асиметричності присутня")
    else:
        print("Властивость асиметричності відсутня")
    print("R2:")
    if r2_asym:
        print("Властивість сильної асиметричності присутня")
    else:
        print("Властивость асиметричності відсутня")
    print()
    print("Зв'язність:")
    print()
    print("R1:")
    if r1_strong_con:
        print("Властивість сильної зв'язності присутня")
    elif r1_slight_con:
        print("Властивість слабкої зв'язності присутня")
    else:
        print("Властивість зв'язності відсутня")
    print("R2:")
    if r2_strong_con:
        print("Властивість сильної зв'язності присутня")
    elif r2_slight_con:
        print("Властивість слабкої зв'язності присутня")
    else:
        print("Властивість рефлексивності відсутня")
    print()
    print("Транзитивність:")
    print()
    print("R1:")
    if r1_trans:
        print("Властивість сильної транзитивності присутня")
    else:
        print("Властивість транзитивності відсутності")
    print("R2:")
    if r2_trans:
        print("Властивість сильної транзитивності присутня")
    else:
        print("Властивість транзитивності відсутня")
