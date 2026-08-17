from collections import Counter


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    normalized_word = word.casefold()
    word_count = Counter(normalized_word)

    result = []

    for candidate in candidates:
        normalized_candidate = candidate.casefold()

        if normalized_candidate == normalized_word:
            continue

        if Counter(normalized_candidate) == word_count:
            result.append(candidate)

    return result