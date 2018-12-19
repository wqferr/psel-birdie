import pandas as pd


def main():
	data = pd.read_csv('data_estag_ds.tsv', sep='\t')
	sample = data.sample(n=500).TITLE
	sample.to_csv('sample.csv', index=False)


if __name__ == '__main__':
	main()