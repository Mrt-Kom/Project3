from flask import Flask, render_template,request

app=Flask(__name__)
developer_name = "E2127- Murat"
def millisecond_conventer(millisec):
    value = int(millisec)
    if value < 1000:
        return f"just {value} millisecond/s"
    else:
        hour = value // 3600000
        minute = (value - (hour * 3600000)) // 60000
        second = (value - (hour * 3600000) - (minute * 60000)) // 1000
        if hour and minute and second:
            return f"{hour} hour/s {minute} minute/s {second} second/s"
        elif hour and minute:
            return f"{hour} hour/s {minute} minute/s"        
        if hour and second:
            return f"{hour} hour/s {second} second/s"
        elif minute and second:
            return f"{minute} minute/s {second} second/s"        
        elif hour:
            return f"{hour} hour/s"
        elif minute:
            return f"{minute} minute/s"
        elif second:
            return f"{second} second/s"

@app.route("/", methods=["GET"])
def main_get():
    return render_template("index.html", developer_name = developer_name, not_valid = False)    

@app.route("/", methods=["POST"])
def main_post():
    second = request.form["number"]
    if not second.isdecimal():
        return render_template("index.html", developer_name = developer_name, not_valid = True)
    
    second_int = int(second)
    if not second_int > 0:
        return render_template("index.html", developer_name = developer_name, not_valid = True)
    return render_template("result.html" , developer_name = developer_name, milliseconds = second, result = millisecond_conventer(second))
 
if __name__ == "__main__":
    app.run(debug= True)           
            
            