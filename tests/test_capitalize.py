from pydemo.capitalize import capital_case, lower_case

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_lower_case():
    assert lower_case('SEMAPHORE') == 'semaphore'
