pragma solidity 0.4.24;

contract W3Pass{

    struct Credential{
        string domain;
        string login;
        string password;

    }

    mapping(address => Credential[]) public credentials;

    function addCredentials(address owner, string _domain, string _login, string _password) public {
    owner == address(this);
    credentials[owner].push(Credential(_domain, _login, _password));
    }

    function getCredentialsCount(address addressQuery) public view {
    credentials[addressQuery].length;
    }
}
