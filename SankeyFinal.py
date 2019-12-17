import plotly.graph_objects as go
import pandas as pd

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def loadData(fileName):
    fileName = "/home/hal/Documents/PythonScripts/Sankey/" + fileName
    data = pd.read_csv(fileName, sep=',',header=None)
    for i in range(len(data.values)):
        try:
            int(data.values[i,0])
            id.append(data.values[i,0])
            lables.append(data.values[i,1])
            sourceValues.append(data.values[i,2])
            colours.append(data.values[i,3])
        except:
            pass

def loadCat(fileName, cat):
    fileName = "/home/hal/Documents/PythonScripts/Sankey/" + fileName
    data = pd.read_csv(fileName, sep=',',header=None)
    for i in range(len(data.values)):
        cat.append(data.values[i])

def loadLinkData(fileName):
    fileName = "/home/hal/Documents/PythonScripts/Sankey/" + fileName
    data = pd.read_csv(fileName, sep=',',header=None)
    for i in range(len(data.values)): #loop through all entries
        if is_number(data.values[i,0]): #if source is number
            sources.append(data.values[i,0]) #add source and target from file to list
            targets.append(data.values[i,1])

            if not is_number(data.values[i,2]): #if value is not a number
                if data.values[i,2] == "all":
                    if int(data.values[i,0]) < 14: #if id is input
                        values.append(sourceValues[int(data.values[i,0])])
                    else:
                        values.append(sourceValues[int(data.values[i,1])])
                else:
                    values.append(sourceValues[int(data.values[i,1])])
            else:
                values.append(data.values[i,2])

            if not isinstance(data.values[i,3], str):
                linkColour.append("lightgray")
            else:
                linkColour.append(data.values[i,3])


id = []
lables = []
sourceValues = []
colours = []

sources = []
targets = []
values = []
linkColour = []

notSolo = []

Renewables = []
FossilFuels = []

sumRenew = 0

loadData('InputData.csv')
loadData('OutputData.csv')
loadData('Categories.csv')

loadLinkData('LinkData.csv')

loadCat("Renewables.csv", Renewables)
loadCat("FossilFuels.csv", FossilFuels)

print(sourceValues)

'''
#Catagorise renewalbes
for i in range(len(sources)):
    if sources[i] == sources[i]:
        print(lables[int(sources[i])])
        print(Renewables)
        if lables[int(sources[i])] in Renewables:
            sumRenew += float(values[i])
            sources.append(44)
            targets.append(int(sources[i]))
            values.append(sourceValues[int(sources[i])])
            linkColour.append("")
        elif lables[int(sources[i])] in FossilFuels:
            pass
            #print("that")
        else:
            #print("other")
            pass
'''
'''
for i in range(len(sources)): #Finds links that only go to one location
    for j in range(len(sources)):
        if i != j:
            if sources[i] == sources[j]:
                notSolo.append(i)
'''

for i in range(len(sources)): #Sets links to source colour
    if i not in notSolo:
        if is_number(sources[i]) and sources[i] == sources[i]:
            linkColour[i] = colours[int(sources[i])]

'''
for i in range(len(values)):
    if not is_number(values[i]):
        linkColour[i] = colours[int(sources[i])]
'''
for i in range(len(colours)): #Make begining of link darker
    if colours[i][0] == "#":


        r = int(colours[i][1:3], 16)
        g = int(colours[i][3:5], 16)
        b = int(colours[i][5:7], 16)

        brightnessScale = float(r+g+b)/1000*1.4
        '''
        r *= brightnessScale
        g *= brightnessScale
        b *= brightnessScale
        '''


        if r > g and r > b: #Reduces only weaker colours
            #r *= brightnessScale*1.4
            g *= brightnessScale
            b *= brightnessScale
        elif g > r and g > b:
            r *= brightnessScale
            #g *= brightnessScale*1.4
            b *= brightnessScale
        elif b > r and b > g:
            r *= brightnessScale
            g *= brightnessScale
            #b *= brightnessScale*1.4
        else:
            r *= brightnessScale
            g *= brightnessScale
            b *= brightnessScale



        temp = str(hex(int(r)))[2:] + str(hex(int(g)))[2:] + str(hex(int(b)))[2:]

        colours[i] = "#" + temp

fig = go.Figure(data=[go.Sankey(
    domain = dict(
      x =  [0,1],
      y =  [0,1]
    ),
    orientation = "h",
    valueformat = ".00f",
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0),
      label = lables,
      color = colours
    ),
    link = dict(
      source = sources,
      target = targets,
      value = values,
      color = linkColour
  ))])

fig.update_layout(title_text="Energy Diagram", font = dict(
      size = 14,
      color = 'black',
      family = "Arial"
    ))
fig.show()
