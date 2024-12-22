def parse_gene_paths(table_text : str) -> dict:
    gens_in_path = {}
    rows = table_text.strip().split("\n")

    for row in rows:
        cells = row.split("\t")
        path_parts = cells[0].split("_")
        gens = [gen for gen in cells[2:] if gen]

        for path in path_parts:
            for gen in gens:
                key = f"{path}{gen}"
                gens_in_path[key] = gens_in_path.get(key, 0) + 1

    return gens_in_path


def count_paths_for_gene(gene_in_path : dict, 
                         gene : str, 
                         path_part : str) -> int:
    return gene_in_path.get(f"{path_part}{gene}", 0)