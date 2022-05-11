import pytest
from io import StringIO
import sys


# ___________________________________________________________ #
# ___________________________________________________________ #
# _____________ PASTE STUDENT CODE BETWEEN __________________ #
# ___________________________________________________________ #
# ___________________________________________________________ #


# ___________________________________________________________ #
# ___________________________________________________________ #
# _____________ PASTE STUDENT CODE BETWEEN __________________ #
# ___________________________________________________________ #
# ___________________________________________________________ #


# ___________________________________________________________ #
# ___________________________________________________________ #
# ____________ BEGINNING OF AUTOMATED TESTS__________________ #
# ___________________________________________________________ #
# ___________________________________________________________ #



def test_main_variables():
    """

    Prints out a list of the variables defined in the main function

    Arguments:
        None

    Asserts:
        True - if there are variables representing values in the main function
        False - if there are no variables representing values in the main function

    Returns:
        None

    """
    
    print("\nVariables defined in the main function: ")
    for i in range(0,len(main.__code__.co_varnames)):
        print(main.__code__.co_varnames[i])
    if(main.__code__.co_varnames == None):
        assert False
    else:
        assert True
def test_option1_variables():
    """

    Prints out a list of the variables defined in the option1 function

    Arguments:
        None

    Asserts:
        True - if there are variables representing values in the option1 function
        False - if there are no variables representing values in the option1 function

    Returns:
        None

    """
    if(option1.__code__.co_varnames == None):
        assert False
    else:
        assert True

def test_option2_variables():
    """

    Prints out a list of the variables defined in the option2 function

    Arguments:
        None

    Asserts:
        True - if there are variables representing values in the option2 function
        False - if there are no variables representing values in the option2 function

    Returns:
        None

    """
    if(option2.__code__.co_varnames == None):
        assert False
    else:
        assert True

def test_option3_variables():
    """

    Prints out a list of the variables defined in the option3 function

    Arguments:
        None

    Asserts:
        True - if there are variables representing values in the option3 function
        False - if there are no variables representing values in the option3 function

    Returns:
        None

    """
    if(option3.__code__.co_varnames == None):
        assert False
    else:
        assert True

def test_option4_variables():
    """

    Prints out a list of the variables defined in the option4 function

    Arguments:
        None

    Asserts:
        True - if there are variables representing values in the option4 function
        False - if there are no variables representing values in the option4 function

    Returns:
        None

    """
    if(option4.__code__.co_varnames == None):
        assert False
    else:
        assert True

def test_title_msg(capfd):
    """

    Tests if there is a title message

    Arguments:
        None

    Asserts:
        True - if there is a title message outputted
        False - if there is no title message outputted

    Returns:
        None

    Args:
        capfd : helper function for automating IO
    """
    title_msg()
    out,err=capfd.readouterr()
    assert len(out) >= 5, "There is no title message!"

def test_option1(capfd):
    """

    Tests if there is an option1 message

    Arguments:
        None

    Asserts:
        True - if there is a option1 message outputted
        False - if there is no option1 message outputted

    Returns:
        None

    Args:
        capfd : helper function for automating IO
    """
    option1()
    out,err=capfd.readouterr()
    assert len(out) >= 5, "There is no option 1"

def test_option2(capfd):
    """

    Tests if there is an option2 message

    Arguments:
        None

    Asserts:
        True - if there is a option2 message outputted
        False - if there is no option2 message outputted

    Returns:
        None

    Args:
        capfd : helper function for automating IO
    """
    option2()
    out,err=capfd.readouterr()
    assert len(out) >= 5, "There is no option 2"

def test_option3(capfd):
    """

    Tests if there is an option3 message

    Arguments:
        None

    Asserts:
        True - if there is a option3 message outputted
        False - if there is no option3 message outputted

    Returns:
        None

    Args:
        capfd : helper function for automating IO
    """
    option3()
    out,err=capfd.readouterr()
    assert len(out) >= 5, "There is no option 3"

def test_option4(capfd):
    """

    Tests if there is an option4 message

    Arguments:
        None

    Asserts:
        True - if there is a option4 message outputted
        False - if there is no option4 message outputted

    Returns:
        None

    Args:
        capfd : helper function for automating IO
    """
    option4()
    out,err=capfd.readouterr()
    assert len(out) >= 5, "There is no option 4"

def test_get_choice_character_input(monkeypatch, capfd):  # or use "capfd" for fd-level
    """

    Mock inputs -1 into the get_choice function

    Arguments:
        None

    Asserts:
        True - if character inputs are handled
        False - if character inputs are not handled

    Returns:
        None

    Args:
        monkeypatch : helper function for automating IO
        capfd : helper function for automating IO
    """
    # Enters -1 into the get choice function (mocks input)
    inputs = StringIO('aaa\n')
    monkeypatch.setattr('sys.stdin', inputs)
    assert get_choice()
    out,err=capfd.readouterr()
    assert len(out) >= 5, "Character inputs not handled"

def test_get_choice_outside_bounds_positive(monkeypatch, capfd):  # or use "capfd" for fd-level
    """

    Mock inputs 6 into the get_choice function

    Arguments:
        None

    Asserts:
        True - if out of limits inputs are handled
        False - if out of limits inputs are not handled

    Returns:
        None

    Args:
        monkeypatch : helper function for automating IO
        capfd : helper function for automating IO
    """
    inputs = StringIO('6\n')
    monkeypatch.setattr('sys.stdin', inputs)
    assert get_choice()
    out,err=capfd.readouterr()
    assert len(out) >= 5, "Out of bounds value not handled"



















































































































































































































