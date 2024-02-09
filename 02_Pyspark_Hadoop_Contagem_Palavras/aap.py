import sys

from pyspark import SparkContext, SparkConf

if __name__ == '__main__':

	#Criar SparkContext
	conf = SparkConf().setAppName("Conta Palavras").set("master", "local")
	sc = SparkContext(conf = conf)

	#Carregar o arquivo
	palavras = sc.textFile("/home/hadoop/input.txt").flatMap(lambda line: line.split(" "))

	#Conta a ocorrência de palavras
	contagem = palavras.map(lambda palavra: (palavra, 1)).reduceByKey(lambda a,b: a + b)

	#Salvar o resultado
	contagem.saveAsTextFile("/home/hadoop/saida")