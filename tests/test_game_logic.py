import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_invalid_guess_string():
    # Non-numeric string should return "Too Low"
    result = check_guess("abc", 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_invalid_secret_string():
    # Non-numeric string secret should return "Too Low"
    result = check_guess(50, "xyz")
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_none_guess():
    # None guess should return "Too Low"
    result = check_guess(None, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_string_numbers():
    # String representation of numbers should work
    result = check_guess("50", "50")
    assert result == ("Win", "🎉 Correct!")

def test_boundary_values():
    # Test with zero
    result = check_guess(0, 0)
    assert result == ("Win", "🎉 Correct!")

def test_negative_numbers():
    # Test with negative numbers
    result = check_guess(-10, -20)
    assert result == ("Too High", "📉 Go LOWER!")
