import React, { useState }  from "react";
import './App.css';
import CopyIcon from './copyicon.png'
import ExternalLink from './externallink.png'
import { ethers } from "ethers";

const provider = new ethers.providers.Web3Provider(window.ethereum);

const data = [
  { website: "google.co.in", email: "test@gmail.com", password: "8282", id: 1 },
  { website: "coinlist.co", email: "test@gmail.com", password: "6969", id: 2 },
  { website: "facebook.com", email: "prathameshnate321@gmail.com", password: "666", id: 3 },
  { website: "kucoin.com", email: "prathameshnate.sprints@gmail.com", password: "777", id: 4 }, 
  { website: "gate.com", email: "prathameshnate.sfdc@gmail.com", password: "555", id: 5 }, 
];

let isRevealed;

export default function OurApp() {
  return (
    <>
      <MetamaskButton/>
      <Header/>
      <DataTable/>
      <SaveMorePasswords/>
    </>
  )
}

function MetamaskButton() {
  return <button className="metamaskbutton" id="connectButton" onClick={handleMetamaskButton}>Login via Metamask</button>
}

function Header() {
  return <h2 className="heading">User Dashboard</h2>
}

function DataTable() {

  return (
    <>
      <table className="datatable" align="center">
        <thead className="tablehead">
          <tr>
            <th>Websites</th>
            <th>Login</th>
            <th>Password</th>
            <th>Retrieve</th>
          </tr>
        </thead>
          <tbody className="tablebody">
          {data.map((val,key) => {
            return(
              <tr key={key}>
                <td align="center">
                  <a href={`https://${val.website}`} target="_blank" rel="noopener noreferrer">{val.website}</a>
                  <img alt={val.website} src={ExternalLink}></img>
                </td>
                <td align="center">
                  {val.email}
                  <img alt="Copy" src={CopyIcon} onClick={() => handleClick(val.website,"email")} className="copyicon"></img>
                </td>
                <td align="center">
                  {val.password}
                  <img alt="Copy" src={CopyIcon} onClick={() => handleClick( val.website,"password")} className="copyicon"></img>
                </td>
                <td align="center">
                  <button className="revealbutton" id={`button{val.id}`}onClick={() => handleReveal(isRevealed, val.id)}>{isRevealed?(<>Hide</>):(<>Reveal</>)}</button>
                </td>
              </tr>
            )
          })
          }
          </tbody>        
      </table>
    </>
  )
}

function SaveMorePasswords() {
  const [show, setShow] = useState(false);
  return(
    <div>
      <button className="savemorepasswords" onClick={() => setShow(!show)}>Save More Passwords</button>
      {show && (
        <>
        <br/>
        <input placeholder="Enter Website"/>
        <input placeholder="Enter Login"/>
        <input type="password" placeholder="Enter password"/>
        </>
      )}
    </div>
  )

}

function handleClick(data, source) {
  source === "email" ? alert(`Email copied for ${data}`) : alert(`Password copied for ${data}`);
  
}

function handleReveal(flag, id) {
  isRevealed = !flag;
  console.log(isRevealed+' '+id);
  return isRevealed;
}

function handleMetamaskButton() {
  window.ethereum ?
  window.ethereum.request({method: "eth_requestAccounts"}).then((accounts) => {
  
    console.log(accounts[0])
      
  }).catch((err) => console.log(err))
: console.log("Please install MetaMask");

try {
  
  provider.request({
    method: 'wallet_switchEthereumChain',
    params: [{ chainId: "0x7E5"}],
  });
  console.log("You have switched to the right network")
  
} catch (switchError) {
  
  if (switchError.code === 4902) {
   console.log("Please add the Polygon network to MetaMask")
  }
  console.log("Cannot switch to the network")
  
}

try {
  provider.request({
    method: 'wallet_addEthereumChain',
    params: [
        {
          chainId: '0x89', 
          chainName:'Edgeware',
          rpcUrls:['https://edgeware-evm.jelliedowl.net/'],                   
          blockExplorerUrls:['https://edgscan.live/'],  
          nativeCurrency: {
            name: 'Edgeware', 
            symbol:'EDG',   
            decimals: 18
          }     
        }
      ]});
} catch (err) {
   console.log(err);
}

}

//TODO AFter a certain interval, the string will go back to ****
