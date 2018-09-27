def parseExpression(expr, variables):
    result, charIndex = getValue(expr, 0)
    while charIndex < len(expr):
        char = expr[charIndex]
        value, offset = getValue(expr, charIndex + 1)
        if char == "+": result += value
        if char == "*": result *= value
        charIndex += offset + 1
    return result

def getValue(expr, index):
    if expr[index] == "(":
        localExpression = getLocalExpression(expr, index)
        value = parseExpression(localExpression, variables)
        charCount = len(localExpression) + 2
    else:
        variableName = getVariableName(expr, index)
        value = variables[variableName]
        charCount = len(variableName)
    return value, charCount

def getVariableName(expr, firstCharIndex):
    charCount = len(expr)
    char = expr[firstCharIndex]
    lastCharIndex = firstCharIndex
    while char not in ("*", "+", ")"):
        lastCharIndex += 1
        if lastCharIndex < charCount:
            char = expr[lastCharIndex]
        else:
            break
    return expr[firstCharIndex:lastCharIndex]

def getLocalExpression(expr, openBracketIndex):
    localExpressionCount = 1
    closeBracketIndex = openBracketIndex + 1
    while localExpressionCount:
        char = expr[closeBracketIndex]
        if char == "(": localExpressionCount += 1
        if char == ")": localExpressionCount -= 1
        closeBracketIndex += 1
    return expr[openBracketIndex + 1:closeBracketIndex - 1]
