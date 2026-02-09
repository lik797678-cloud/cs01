import React from 'react';

const BeerMarket = ({ beers }) => {
    return (
        <div className="beer-market">
            <h1>Available Beers for Trading</h1>
            <ul>
                {beers.map((beer, index) => (
                    <li key={index}>
                        <h2>{beer.name}</h2>
                        <p>Type: {beer.type}</p>
                        <p>ABV: {beer.abv}%</p>
                        <p>Description: {beer.description}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default BeerMarket;
