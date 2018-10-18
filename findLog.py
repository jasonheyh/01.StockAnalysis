import csv

result_csv = open("/Users/jiangyantao/Downloads/no_refered_pages_20180712121448/no_refered_pages_20180712121448.csv")
result_log = open("/Users/jiangyantao/Downloads/no_refered_pages_20180712121448/no_refered_pages_20180712121448_チェックリンク元リスト.log")

logResult = []
for lineLog in result_log:
    logResult.append(lineLog)

for lineCsv in result_csv:
    for lineLog in logResult:
        lineCsv = lineCsv.replace("\n","").replace("\"","")
        lineLog = lineLog.replace("\n","").replace("\"","")
        if lineCsv in lineLog:
            print(lineCsv)
            break
result_csv.close()
result_log.close()
print("処理終わりました。")

