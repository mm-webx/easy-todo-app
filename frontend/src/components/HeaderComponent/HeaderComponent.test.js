import React from 'react';
import ReactDOM from 'react-dom';
import HeaderComponent from './HeaderComponent'

it('renders title', () => {
  const { getByText } = render(<HeaderComponent title="test"/>);
  expect(getByText('test')).toBeInTheDocument();
});
