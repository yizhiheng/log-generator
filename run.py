import datetime
import fileinput

def main():
	
	message = ""

	for line in fileinput.input():
		message += line

	quote = "\""
	message = message.replace("\n", "\\n")
	message = message.replace("\t", "\\t")
	message = message.replace(quote, "\\" + quote)


	output = "{\"timestamp\":\"" + datetime.datetime.utcnow().isoformat() + "\",\"message\":\"" + message + "\"}"

	print output

if __name__ == "__main__":
	main()
