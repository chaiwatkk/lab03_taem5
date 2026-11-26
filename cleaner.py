def clean_text(text):
	"""Trim leading/trailing whitespace and collapse internal whitespace."""
	return " ".join(text.split())
