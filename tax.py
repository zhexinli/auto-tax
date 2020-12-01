#输入全年应纳税综合所得，输出税后年收入
import sys

def tax(x):
    stage = (36000, 144000, 300000, 420000, 660000, 960000)
    if x <= stage[0]: return 0.03 * x
    if x <= stage[1]: return 0.1 * (x - stage[0]) + tax(stage[0])
    if x <= stage[2]: return 0.2 * (x - stage[1]) + tax(stage[1])
    if x <= stage[3]: return 0.25 * (x - stage[2]) + tax(stage[2])
    if x <= stage[4]: return 0.3 * (x - stage[3]) + tax(stage[3])
    if x <= stage[5]: return 0.35 * (x - stage[4]) + tax(stage[4])
    else: return 0.45 * (x - stage[5]) + tax(stage[5])


if __name__ == '__main__':
    income = int(sys.argv[1])
    taxes = tax(income)
    income -= taxes
    print("全年应纳税额%.2f元，税后所得%.2f元。" % (taxes, income))



    
