import json
from pprint import pprint

with open("../resultados-finais+participantes-info-ordered.json") as f, open(
    "RESULTADOS_FINAIS_TMP.md", "w"
) as r:
    r.write(
        "| ranking | participante | p99 | bônus p99 (%) | multa ($) | lucro | submissão |\n"
    )
    r.write("| -- | -- | -- | -- | -- | -- | -- |\n")
    ranking = 0
    results = json.loads(f.read())
    for result in results:
        try:
            if not result["erro_na_execucao"] and "resultado_final" in result:
                resultado_final = result["resultado_final"]
                local_ranking = resultado_final["total_liquido"]

                if resultado_final["total_liquido"] == 0:
                    local_ranking = "--"
                else:
                    ranking += 1
                    local_ranking = ranking

                participante = (
                    f"{resultado_final["participante"][:12]}..."
                    if len(resultado_final["participante"]) > 15
                    else resultado_final["participante"]
                )
                link_dir = f"[dir→](./participantes/{resultado_final["participante"]})"
                line = f"| {local_ranking} | {participante} | {resultado_final["p99"]["valor"]} | {resultado_final["p99"]["bonus"]} | {resultado_final["multa"]["total"]} | {resultado_final["total_liquido"]} | {link_dir} |\n"
                r.write(line)
        except Exception as ex:
            print("==============================")
            pprint(ex)
            pprint(result)
