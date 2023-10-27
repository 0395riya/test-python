import React from 'react'






const Data = () => {
    const names = ['shyla', 'mihir', 'jyoti', 'sheetal', 'pravesh']
    const listItem = names.map((name, ind) => {
        return (
        <li key={ind}>{name}</li>
        )
    })
   

    return (
        <div>
        <ul>{listItem}</ul>
     
        </div>
        
    )
}



export default Data