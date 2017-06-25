import clusterpy
import sys

# python laura.py conseq
conseq = int(sys.argv[1])
numArea = [4, 5, 6, 7]
numReg = [3, 7, 11]
numRho = [0.5, 0.7, 0.9]

# import itertools
#list(itertools.product(numArea, numReg, numRho, range(1,6),range(1,3)))
exp=[(4, 3, 0.5, 1, 1), (4, 3, 0.5, 1, 2), (4, 3, 0.5, 2, 1), (4, 3, 0.5, 2, 2),
(4, 3, 0.5, 3, 1), (4, 3, 0.5, 3, 2), (4, 3, 0.5, 4, 1), (4, 3, 0.5, 4, 2),
(4, 3, 0.5, 5, 1), (4, 3, 0.5, 5, 2), (4, 3, 0.7, 1, 1), (4, 3, 0.7, 1, 2),
(4, 3, 0.7, 2, 1), (4, 3, 0.7, 2, 2), (4, 3, 0.7, 3, 1), (4, 3, 0.7, 3, 2),
(4, 3, 0.7, 4, 1), (4, 3, 0.7, 4, 2), (4, 3, 0.7, 5, 1), (4, 3, 0.7, 5, 2),
(4, 3, 0.9, 1, 1), (4, 3, 0.9, 1, 2), (4, 3, 0.9, 2, 1), (4, 3, 0.9, 2, 2),
(4, 3, 0.9, 3, 1), (4, 3, 0.9, 3, 2), (4, 3, 0.9, 4, 1), (4, 3, 0.9, 4, 2),
(4, 3, 0.9, 5, 1), (4, 3, 0.9, 5, 2), (4, 7, 0.5, 1, 1), (4, 7, 0.5, 1, 2),
(4, 7, 0.5, 2, 1), (4, 7, 0.5, 2, 2), (4, 7, 0.5, 3, 1), (4, 7, 0.5, 3, 2),
(4, 7, 0.5, 4, 1), (4, 7, 0.5, 4, 2), (4, 7, 0.5, 5, 1), (4, 7, 0.5, 5, 2),
(4, 7, 0.7, 1, 1), (4, 7, 0.7, 1, 2), (4, 7, 0.7, 2, 1), (4, 7, 0.7, 2, 2),
(4, 7, 0.7, 3, 1), (4, 7, 0.7, 3, 2), (4, 7, 0.7, 4, 1), (4, 7, 0.7, 4, 2),
(4, 7, 0.7, 5, 1), (4, 7, 0.7, 5, 2), (4, 7, 0.9, 1, 1), (4, 7, 0.9, 1, 2),
(4, 7, 0.9, 2, 1), (4, 7, 0.9, 2, 2), (4, 7, 0.9, 3, 1), (4, 7, 0.9, 3, 2),
(4, 7, 0.9, 4, 1), (4, 7, 0.9, 4, 2), (4, 7, 0.9, 5, 1), (4, 7, 0.9, 5, 2),
(4, 11, 0.5, 1, 1), (4, 11, 0.5, 1, 2), (4, 11, 0.5, 2, 1), (4, 11, 0.5, 2, 2),
(4, 11, 0.5, 3, 1), (4, 11, 0.5, 3, 2), (4, 11, 0.5, 4, 1), (4, 11, 0.5, 4, 2),
(4, 11, 0.5, 5, 1), (4, 11, 0.5, 5, 2), (4, 11, 0.7, 1, 1), (4, 11, 0.7, 1, 2),
(4, 11, 0.7, 2, 1), (4, 11, 0.7, 2, 2), (4, 11, 0.7, 3, 1), (4, 11, 0.7, 3, 2),
(4, 11, 0.7, 4, 1), (4, 11, 0.7, 4, 2), (4, 11, 0.7, 5, 1), (4, 11, 0.7, 5, 2),
(4, 11, 0.9, 1, 1), (4, 11, 0.9, 1, 2), (4, 11, 0.9, 2, 1), (4, 11, 0.9, 2, 2),
(4, 11, 0.9, 3, 1), (4, 11, 0.9, 3, 2), (4, 11, 0.9, 4, 1), (4, 11, 0.9, 4, 2),
(4, 11, 0.9, 5, 1), (4, 11, 0.9, 5, 2), (5, 3, 0.5, 1, 1), (5, 3, 0.5, 1, 2),
(5, 3, 0.5, 2, 1), (5, 3, 0.5, 2, 2), (5, 3, 0.5, 3, 1), (5, 3, 0.5, 3, 2),
(5, 3, 0.5, 4, 1), (5, 3, 0.5, 4, 2), (5, 3, 0.5, 5, 1), (5, 3, 0.5, 5, 2),
(5, 3, 0.7, 1, 1), (5, 3, 0.7, 1, 2), (5, 3, 0.7, 2, 1), (5, 3, 0.7, 2, 2),
(5, 3, 0.7, 3, 1), (5, 3, 0.7, 3, 2), (5, 3, 0.7, 4, 1), (5, 3, 0.7, 4, 2),
(5, 3, 0.7, 5, 1), (5, 3, 0.7, 5, 2), (5, 3, 0.9, 1, 1), (5, 3, 0.9, 1, 2),
(5, 3, 0.9, 2, 1), (5, 3, 0.9, 2, 2), (5, 3, 0.9, 3, 1), (5, 3, 0.9, 3, 2),
(5, 3, 0.9, 4, 1), (5, 3, 0.9, 4, 2), (5, 3, 0.9, 5, 1), (5, 3, 0.9, 5, 2),
(5, 7, 0.5, 1, 1), (5, 7, 0.5, 1, 2), (5, 7, 0.5, 2, 1), (5, 7, 0.5, 2, 2),
(5, 7, 0.5, 3, 1), (5, 7, 0.5, 3, 2), (5, 7, 0.5, 4, 1), (5, 7, 0.5, 4, 2),
(5, 7, 0.5, 5, 1), (5, 7, 0.5, 5, 2), (5, 7, 0.7, 1, 1), (5, 7, 0.7, 1, 2),
(5, 7, 0.7, 2, 1), (5, 7, 0.7, 2, 2), (5, 7, 0.7, 3, 1), (5, 7, 0.7, 3, 2),
(5, 7, 0.7, 4, 1), (5, 7, 0.7, 4, 2), (5, 7, 0.7, 5, 1), (5, 7, 0.7, 5, 2),
(5, 7, 0.9, 1, 1), (5, 7, 0.9, 1, 2), (5, 7, 0.9, 2, 1), (5, 7, 0.9, 2, 2),
(5, 7, 0.9, 3, 1), (5, 7, 0.9, 3, 2), (5, 7, 0.9, 4, 1), (5, 7, 0.9, 4, 2),
(5, 7, 0.9, 5, 1), (5, 7, 0.9, 5, 2), (5, 11, 0.5, 1, 1), (5, 11, 0.5, 1, 2),
(5, 11, 0.5, 2, 1), (5, 11, 0.5, 2, 2), (5, 11, 0.5, 3, 1), (5, 11, 0.5, 3, 2),
(5, 11, 0.5, 4, 1), (5, 11, 0.5, 4, 2), (5, 11, 0.5, 5, 1), (5, 11, 0.5, 5, 2),
(5, 11, 0.7, 1, 1), (5, 11, 0.7, 1, 2), (5, 11, 0.7, 2, 1), (5, 11, 0.7, 2, 2),
(5, 11, 0.7, 3, 1), (5, 11, 0.7, 3, 2), (5, 11, 0.7, 4, 1), (5, 11, 0.7, 4, 2),
(5, 11, 0.7, 5, 1), (5, 11, 0.7, 5, 2), (5, 11, 0.9, 1, 1), (5, 11, 0.9, 1, 2),
(5, 11, 0.9, 2, 1), (5, 11, 0.9, 2, 2), (5, 11, 0.9, 3, 1), (5, 11, 0.9, 3, 2),
(5, 11, 0.9, 4, 1), (5, 11, 0.9, 4, 2), (5, 11, 0.9, 5, 1), (5, 11, 0.9, 5, 2),
(6, 3, 0.5, 1, 1), (6, 3, 0.5, 1, 2), (6, 3, 0.5, 2, 1), (6, 3, 0.5, 2, 2),
(6, 3, 0.5, 3, 1), (6, 3, 0.5, 3, 2), (6, 3, 0.5, 4, 1), (6, 3, 0.5, 4, 2),
(6, 3, 0.5, 5, 1), (6, 3, 0.5, 5, 2), (6, 3, 0.7, 1, 1), (6, 3, 0.7, 1, 2),
(6, 3, 0.7, 2, 1), (6, 3, 0.7, 2, 2), (6, 3, 0.7, 3, 1), (6, 3, 0.7, 3, 2),
(6, 3, 0.7, 4, 1), (6, 3, 0.7, 4, 2), (6, 3, 0.7, 5, 1), (6, 3, 0.7, 5, 2),
(6, 3, 0.9, 1, 1), (6, 3, 0.9, 1, 2), (6, 3, 0.9, 2, 1), (6, 3, 0.9, 2, 2),
(6, 3, 0.9, 3, 1), (6, 3, 0.9, 3, 2), (6, 3, 0.9, 4, 1), (6, 3, 0.9, 4, 2),
(6, 3, 0.9, 5, 1), (6, 3, 0.9, 5, 2), (6, 7, 0.5, 1, 1), (6, 7, 0.5, 1, 2),
(6, 7, 0.5, 2, 1), (6, 7, 0.5, 2, 2), (6, 7, 0.5, 3, 1), (6, 7, 0.5, 3, 2),
(6, 7, 0.5, 4, 1), (6, 7, 0.5, 4, 2), (6, 7, 0.5, 5, 1), (6, 7, 0.5, 5, 2),
(6, 7, 0.7, 1, 1), (6, 7, 0.7, 1, 2), (6, 7, 0.7, 2, 1), (6, 7, 0.7, 2, 2),
(6, 7, 0.7, 3, 1), (6, 7, 0.7, 3, 2), (6, 7, 0.7, 4, 1), (6, 7, 0.7, 4, 2),
(6, 7, 0.7, 5, 1), (6, 7, 0.7, 5, 2), (6, 7, 0.9, 1, 1), (6, 7, 0.9, 1, 2),
(6, 7, 0.9, 2, 1), (6, 7, 0.9, 2, 2), (6, 7, 0.9, 3, 1), (6, 7, 0.9, 3, 2),
(6, 7, 0.9, 4, 1), (6, 7, 0.9, 4, 2), (6, 7, 0.9, 5, 1), (6, 7, 0.9, 5, 2),
(6, 11, 0.5, 1, 1), (6, 11, 0.5, 1, 2), (6, 11, 0.5, 2, 1), (6, 11, 0.5, 2, 2),
(6, 11, 0.5, 3, 1), (6, 11, 0.5, 3, 2), (6, 11, 0.5, 4, 1), (6, 11, 0.5, 4, 2),
(6, 11, 0.5, 5, 1), (6, 11, 0.5, 5, 2), (6, 11, 0.7, 1, 1), (6, 11, 0.7, 1, 2),
(6, 11, 0.7, 2, 1), (6, 11, 0.7, 2, 2), (6, 11, 0.7, 3, 1), (6, 11, 0.7, 3, 2),
(6, 11, 0.7, 4, 1), (6, 11, 0.7, 4, 2), (6, 11, 0.7, 5, 1), (6, 11, 0.7, 5, 2),
(6, 11, 0.9, 1, 1), (6, 11, 0.9, 1, 2), (6, 11, 0.9, 2, 1), (6, 11, 0.9, 2, 2),
(6, 11, 0.9, 3, 1), (6, 11, 0.9, 3, 2), (6, 11, 0.9, 4, 1), (6, 11, 0.9, 4, 2),
(6, 11, 0.9, 5, 1), (6, 11, 0.9, 5, 2), (7, 3, 0.5, 1, 1), (7, 3, 0.5, 1, 2),
(7, 3, 0.5, 2, 1), (7, 3, 0.5, 2, 2), (7, 3, 0.5, 3, 1), (7, 3, 0.5, 3, 2),
(7, 3, 0.5, 4, 1), (7, 3, 0.5, 4, 2), (7, 3, 0.5, 5, 1), (7, 3, 0.5, 5, 2),
(7, 3, 0.7, 1, 1), (7, 3, 0.7, 1, 2), (7, 3, 0.7, 2, 1), (7, 3, 0.7, 2, 2),
(7, 3, 0.7, 3, 1), (7, 3, 0.7, 3, 2), (7, 3, 0.7, 4, 1), (7, 3, 0.7, 4, 2),
(7, 3, 0.7, 5, 1), (7, 3, 0.7, 5, 2), (7, 3, 0.9, 1, 1), (7, 3, 0.9, 1, 2),
(7, 3, 0.9, 2, 1), (7, 3, 0.9, 2, 2), (7, 3, 0.9, 3, 1), (7, 3, 0.9, 3, 2),
(7, 3, 0.9, 4, 1), (7, 3, 0.9, 4, 2), (7, 3, 0.9, 5, 1), (7, 3, 0.9, 5, 2),
(7, 7, 0.5, 1, 1), (7, 7, 0.5, 1, 2), (7, 7, 0.5, 2, 1), (7, 7, 0.5, 2, 2),
(7, 7, 0.5, 3, 1), (7, 7, 0.5, 3, 2), (7, 7, 0.5, 4, 1), (7, 7, 0.5, 4, 2),
(7, 7, 0.5, 5, 1), (7, 7, 0.5, 5, 2), (7, 7, 0.7, 1, 1), (7, 7, 0.7, 1, 2),
(7, 7, 0.7, 2, 1), (7, 7, 0.7, 2, 2), (7, 7, 0.7, 3, 1), (7, 7, 0.7, 3, 2),
(7, 7, 0.7, 4, 1), (7, 7, 0.7, 4, 2), (7, 7, 0.7, 5, 1), (7, 7, 0.7, 5, 2),
(7, 7, 0.9, 1, 1), (7, 7, 0.9, 1, 2), (7, 7, 0.9, 2, 1), (7, 7, 0.9, 2, 2),
(7, 7, 0.9, 3, 1), (7, 7, 0.9, 3, 2), (7, 7, 0.9, 4, 1), (7, 7, 0.9, 4, 2),
(7, 7, 0.9, 5, 1), (7, 7, 0.9, 5, 2), (7, 11, 0.5, 1, 1), (7, 11, 0.5, 1, 2),
(7, 11, 0.5, 2, 1), (7, 11, 0.5, 2, 2), (7, 11, 0.5, 3, 1), (7, 11, 0.5, 3, 2),
(7, 11, 0.5, 4, 1), (7, 11, 0.5, 4, 2), (7, 11, 0.5, 5, 1), (7, 11, 0.5, 5, 2),
(7, 11, 0.7, 1, 1), (7, 11, 0.7, 1, 2), (7, 11, 0.7, 2, 1), (7, 11, 0.7, 2, 2),
(7, 11, 0.7, 3, 1), (7, 11, 0.7, 3, 2), (7, 11, 0.7, 4, 1), (7, 11, 0.7, 4, 2),
(7, 11, 0.7, 5, 1), (7, 11, 0.7, 5, 2), (7, 11, 0.9, 1, 1), (7, 11, 0.9, 1, 2),
(7, 11, 0.9, 2, 1), (7, 11, 0.9, 2, 2), (7, 11, 0.9, 3, 1), (7, 11, 0.9, 3, 2),
(7, 11, 0.9, 4, 1), (7, 11, 0.9, 4, 2), (7, 11, 0.9, 5, 1), (7, 11, 0.9, 5, 2)]

tup = exp[conseq]
area = tup[0]
reg = tup[1]
rho = tup[2]
inst = tup[3]
form = tup[4]


lay = clusterpy.importArcData("pregInstances/preg"+str(area*area)+"-"+str(rho)+"-"+str(inst))

#f.write("n p rho instance best-bound best-int time sol best-boundCP best-intCP timeCP solCP\n")

#generate .txt file
if form==1: # without

    f = open(str(conseq)+"-"+str(area)+"-"+str(reg)+"-"+str(rho)+"-"+str(inst)+"-E"+".txt","w")
    f.write(str(area*area)+" "+str(reg)+" "+str(rho)+" "+str(inst)+" E ")
    f.close()

    # WITHOUT CUTTING PLANES
    lay.cluster('pRegionsExact',['SAR1'],p=reg, rho=rho, inst=inst, conseq=conseq)

    pregExp=lay.fieldNames[-1]
    output=lay.outputCluster[pregExp]
    f = open(str(conseq)+"-"+str(area)+"-"+str(reg)+"-"+str(rho)+"-"+str(inst)+"-E"+".txt","a")
    f.write(str(output["bestBound"])+"  "+str(output["objectiveFunction"])+"  "+str(output["running time"])+" ")
    f.close()
else:

    f = open(str(conseq)+"-"+str(area)+"-"+str(reg)+"-"+str(rho)+"-"+str(inst)+"-CP"+".txt","w")
    f.write(str(area*area)+" "+str(reg)+" "+str(rho)+" "+str(inst)+" CP ")
    f.close()

    # WITH CUTTING PLANES
    lay.cluster('pRegionsExactCP',['SAR1'],p=reg, rho=rho, inst=inst, conseq=conseq)

    pregExp1=lay.fieldNames[-1]
    output1=lay.outputCluster[pregExp1]
    f = open(str(conseq)+"-"+str(area)+"-"+str(reg)+"-"+str(rho)+"-"+str(inst)+"-CP"+".txt","a")
    f.write(str(output1["bestBound"])+"  "+str(output1["objectiveFunction"])+"  "+str(output1["running time"])+" ")
    f.close()










# create layer
# for i in area:
    # for r in rho:
            # for j in inst:
                    # lay = clusterpy.createGrid(i,i)
                    # lay.generateData("SAR","rook",1,r)
                    # lay.exportArcData("preg"+str(i*i)+"-"+str(r)+"-"+str(j))
